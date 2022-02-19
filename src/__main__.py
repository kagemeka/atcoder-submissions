from __future__ import annotations

import asyncio
import logging
import os

import aiohttp
import atcoder.contest
import atcoder.submission
import filesystem.path

_LOGGER = logging.getLogger(__name__)

_LOGGING_FORMAT = "%(asctime)s %(levelname)s %(pathname)s %(message)s"
logging.basicConfig(
    format=_LOGGING_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S%z",
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
)


ROOT_DIRECTORY = "jp.atcoder"


async def _fetch_detail_and_save(
    session: aiohttp.ClientSession,
    contest_id: str,
    submission_id: str,
) -> None:
    result = await atcoder.submission.fetch_submission_details(
        session,
        contest_id,
        submission_id,
    )
    _save_submission_result(contest_id, result)


async def _fetch_contest_submissions(
    session: aiohttp.ClientSession,
    contest_id: str,
    username: str = "kagemeka",
) -> None:
    params = atcoder.submission.SubmissionsSearchParams(username=username)
    # save_tasks = []
    async for submission in atcoder.submission.fetch_all_submissions(
        session,
        contest_id,
        params,
    ):
        # await asyncio.sleep(0.03)
#         await asyncio.sleep(0.2)
        save_path = _get_save_path(contest_id, submission)
        # print(save_path)
        if os.path.exists(save_path):
            continue
        await _fetch_detail_and_save(
            session,
            contest_id,
            submission.id,
        )
    #     save_tasks.append(
    #         asyncio.create_task(
    #             _fetch_detail_and_save(
    #                 session,
    #                 contest_id,
    #                 submission.id,
    #             )
    #         )
    #     )
    # await asyncio.gather(*save_tasks)


async def _fetch_submissions() -> None:
    async with aiohttp.ClientSession() as session:
        # tasks = []
        async for contest in atcoder.contest.fetch_all_contests(session):
            await _fetch_contest_submissions(session, contest.id)
        #     tasks.append(
        #         asyncio.create_task(
        #             _fetch_contest_submissions(session, contest.id)
        #         )
        #     )
        # await asyncio.gather(*tasks)


def _get_save_path(
    contest_id: str,
    result: atcoder.submission.SubmissionResult,
) -> str:
    return (
        f"{ROOT_DIRECTORY}/{contest_id}/{result.summary.task_id}/"
        f"{result.id}.{result.summary.language.file_extensions[0]}"
    )


def _save_submission_result(
    contest_id: str,
    result: atcoder.submission.SubmissionResult,
) -> None:
    code = result.details.code
    path = _get_save_path(contest_id, result)
    filesystem.path.prepare_directory(path)
    _LOGGER.info(f"save {path}")
    with open(path, mode="w") as f:
        f.write(code)


async def main() -> None:
    await _fetch_submissions()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        exit(0)
