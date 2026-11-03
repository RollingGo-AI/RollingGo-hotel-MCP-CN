from typing import Annotated

from fastmcp import FastMCP
from pydantic import Field

from ..auth import extract_api_key
from ..client import request_api
from ..models import CheckInParam, FilterOptions, HotelTags, model_dump


def register_search_hotels_tool(mcp: FastMCP) -> None:
    @mcp.tool(name="searchHotels")
    async def search_hotels(
        originQuery: Annotated[str, Field(description="用户原始自然语言需求（原句），用于语义理解与召回排序。")],
        place: Annotated[
            str,
            Field(
                description="用于定位检索范围的地点名称。请传“可被地理解析的单一地点文本”，例如“北京”“上海浦东国际机场”“东京迪士尼乐园”“北京市朝阳区三里屯路19号”。"
            ),
        ],
        placeType: Annotated[
            str,
            Field(description="地点类型。仅允许以下值之一：城市、机场、景点、火车站、地铁站、酒店、区/县、详细地址。必须与 place 语义一致。"),
        ],
        checkInParam: Annotated[
            CheckInParam | None,
            Field(
                description="入住参数对象。字段：adultCount（number，默认2）；checkInDate（string，YYYY-MM-DD）；stayNights（number，默认1）。"
            ),
        ] = None,
        countryCode: Annotated[str | None, Field(description="国家二字码（ISO 3166-1 alpha-2，大写），如 CN、US、JP。在跨国家名歧义或明确限定国家时传入。")] = None,
        filterOptions: Annotated[
            FilterOptions | None,
            Field(
                description="基础筛选对象。字段：distanceInMeter（number，距离上限，米）；starRatings（number[]，星级区间 [min,max]，0.0~5.0，步长0.5）。"
            ),
        ] = None,
        hotelTags: Annotated[
            HotelTags | None,
            Field(
                description="标签筛选对象（高阶筛选）。字段：preferredTags（string[]，偏好标签）；requiredTags（string[]，必须命中）；excludedTags（string[]，排除标签）；preferredBrands（string[]，偏好品牌）；maxPricePerNight（number，每晚预算上限，人民币）；minRoomSize（number，最小房间面积，平方米）。"
            ),
        ] = None,
        size: Annotated[int, Field(description="返回酒店数量上限。建议传 5-20 的整数；默认5。")] = 5,
    ) -> dict:
        """
        该工具用于查询全球酒店。根据地点及结构化筛选条件（日期、入住晚数、人数、星级、距离、标签、品牌、预算）
        返回符合条件的酒店候选列表与最低价格，用于酒店初筛与比选。
        """
        api_key = extract_api_key()

        params = {
            "originQuery": originQuery,
            "place": place,
            "placeType": placeType,
            "size": size,
        }

        if checkInParam:
            params["checkInParam"] = model_dump(checkInParam)

        if countryCode:
            params["countryCode"] = countryCode

        if filterOptions:
            params["filterOptions"] = model_dump(filterOptions)

        if hotelTags:
            params["hotelTags"] = model_dump(hotelTags)

        return await request_api("POST", "/hotelsearch", api_key, payload=params)
