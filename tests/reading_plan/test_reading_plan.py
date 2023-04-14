import pytest
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from tests.mocks.reading_plan import (
    mocked_find_news,
    mocked_news_for_available_time,
)


def test_reading_plan_group_news(mocker):
    mocker.patch(
        "tech_news.analyzer.reading_plan.find_news",
        return_value=mocked_find_news,
    )

    assert (
        ReadingPlanService().group_news_for_available_time(10)
        == mocked_news_for_available_time
    )

    with pytest.raises(ValueError):
        ReadingPlanService().group_news_for_available_time(-1)
