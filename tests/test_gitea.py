# MIT licensed
# Copyright (c) 2013-2020 lilydjwg <lilydjwg@gmail.com>, et al.

from flaky import flaky
import pytest
pytestmark = [pytest.mark.asyncio,
              pytest.mark.needs_net]

@flaky(max_runs=10)
async def test_gitea(get_version):
    ver = await get_version("example", {
        "source": "gitea",
        "gitea": "gitea/tea"})
    assert len(ver) == 8
    assert ver.isdigit()

@flaky(max_runs=10)
async def test_gitea_max_tag(get_version):
    assert await get_version("example", {
        "source": "gitea",
        "gitea": "gitea/tea",
        "use_max_tag": True,
    }) == "v0.4.0"

@flaky(max_runs=10)
async def test_gitea_max_tag_with_ignored(get_version):
    assert await get_version("example", {
        "source": "gitea",
        "gitea": "gitea/tea",
        "use_max_tag": True,
        "ignored": "v0.4.0",
    }) == "v0.3.1"

@flaky(max_runs=10)
async def test_gitea_max_tag_with_include(get_version):
    assert await get_version("example", {
        "source": "gitea",
        "gitea": "gitea/tea",
        "use_max_tag": True,
        "include_regex": r'v0\.3.*',
    }) == "v0.3.1"
