import itertools
import pprint
import aiohttp
import asyncio

import os
import sys
import glob
import logging
import atcoder.contest
import typing
import atcoder.submission
import pandas as pd
import dataclasses

_LOGGER = logging.getLogger(__name__)

_LOGGING_FORMAT = "%(asctime)s %(levelname)s %(pathname)s %(message)s"
logging.basicConfig(
    format=_LOGGING_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S%z",
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
)


ROOT_DIRECTORY = "jp.atcoder"


async def _fetch_submissions_for_contest(
    session: aiohttp.ClientSession,
    contest_id: str,
    username: str = "kagemeka",
) -> typing.AsyncIterator[atcoder.submission.SubmissionResult]:
    params = atcoder.submission.SubmissionsSearchParams(username=username)
    async for submission in atcoder.submission.fetch_all_submission_results(
        session,
        contest_id,
        params,
    ):
        await asyncio.sleep(0.03)
        yield submission


@dataclasses.dataclass(frozen=True)
class Submission:
    contest_id: str
    task_id: str
    submission_id: str


def _get_path(submission: Submission) -> str:
    return (
        f"{ROOT_DIRECTORY}/{submission.contest_id}/{submission.task_id}/"
        f"{submission.submission_id}"
    )


async def _fetch_all_submissions() -> typing.List[Submission]:
    async with aiohttp.ClientSession() as session:
        submissions = []
        contests = []
        async for contest in atcoder.contest.fetch_all_contests(session):
            contests.append(contest)

        print(len(contests))
        cnt = 0
        for contest in contests:
            async for submission in _fetch_submissions_for_contest(
                session,
                contest.id,
            ):
                submissions.append(
                    Submission(
                        contest.id,
                        submission.summary.task_id,
                        submission.id,
                    )
                )
                await asyncio.sleep(0.01)
                cnt += 1
                print(cnt, end="\r")
        return submissions


def _find_local_files() -> typing.List[str]:
    return glob.glob(f"{ROOT_DIRECTORY}/**/*.*", recursive=True)


def _prepare_dir(filepath: str) -> None:
    directory = os.path.dirname(os.path.abspath(filepath))
    os.makedirs(directory, exist_ok=True)


def _filter_submissions(
    submissions: typing.List[Submission],
) -> typing.List[atcoder.submission.SubmissionResult]:
    files = set(
        map(
            lambda file: os.path.splitext(file)[0],
            _find_local_files(),
        )
    )
    return [
        submission
        for submission in submissions
        if _get_path(submission) not in files
    ]


def _save_submission_result(
    contest_id: str,
    result: atcoder.submission.SubmissionResult,
) -> None:
    code = result.details.code
    language = result.summary.language
    extension = language.file_extensions[0]
    submission = Submission(
        contest_id,
        result.summary.task_id,
        result.id,
    )
    path = f"{_get_path(submission)}.{extension}"
    _prepare_dir(path)
    # _LOGGER.info(f'save {path}')
    with open(path, mode="w") as f:
        f.write(code)


async def _fetch_detailed_submissions(
    submissions: typing.List[Submission],
) -> None:
    CHUNK_SIZE = 4
    n = len(submissions)
    async with aiohttp.ClientSession() as session:
        for i in range(0, n, CHUNK_SIZE):
            fetches = []
            contest_ids = []
            for submission in submissions[i : i + CHUNK_SIZE]:
                task = asyncio.create_task(
                    atcoder.submission.fetch_submission_details(
                        session,
                        submission.contest_id,
                        submission.submission_id,
                    )
                )
                fetches.append(task)
                contest_ids.append(submission.contest_id)
            results = await asyncio.gather(*fetches)
            await asyncio.sleep(0)
            for contest_id, result in zip(contest_ids, results):
                _save_submission_result(contest_id, result)


async def main() -> None:
    submissions = await _fetch_all_submissions()
    print(len(submissions))
    df = pd.DataFrame(submissions)
    # df.to_csv("data.csv", index=False)
    # df: pd.DataFrame = pd.read_csv("data.csv")
    submissions = [
        Submission(**submission) for submission in df.to_dict(orient="records")
    ]
    submissions = _filter_submissions(submissions)
    await _fetch_detailed_submissions(submissions)


if __name__ == "__main__":
    asyncio.run(main())
