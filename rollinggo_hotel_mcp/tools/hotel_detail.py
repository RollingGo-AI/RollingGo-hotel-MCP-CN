from typing import Annotated, Any, Dict

from fastmcp import FastMCP
from pydantic import Field

from ..auth import extract_api_key
from ..client import request_api
from ..models import DateParam, LocaleParam, OccupancyParam, model_dump


def register_hotel_detail_tool(mcp: FastMCP) -> None:
    @mcp.tool(name="getHotelDetail")
    async def get_hotel_detail(
        hotelId: Annotated[int | None, Field(description="酒店唯一ID。与 name 二选一；若同时传入，优先使用 hotelId（从searchHotels工具获取）。")] = None,
        name: Annotated[str | None, Field(description="酒店名称（模糊匹配）。仅在没有 hotelId 时使用。")] = None,
        dateParam: Annotated[
            DateParam | None,
            Field(
                description="入离店日期对象。字段：checkInDate（string，YYYY-MM-DD，建议传合法未来日期）；checkOutDate（string，YYYY-MM-DD，必须晚于 checkInDate）。"
            ),
        ] = None,
        occupancyParam: Annotated[
            OccupancyParam | None,
            Field(
                description="入住人数与房间数量对象。字段：adultCount（number，默认2）；childCount（number，默认0）；childAgeDetails（number[]，如 [3,5]，长度应与 childCount 一致）；roomCount（number，默认1）。"
            ),
        ] = None,
        localeParam: Annotated[
            LocaleParam | None,
            Field(
                description="区域与币种对象。字段：countryCode（string，ISO 3166-1 alpha-2，默认 CN）；currency（string，ISO 4217，默认 CNY）。"
            ),
        ] = None,
    ) -> dict:
        """
        查询单个酒店实时房型与价格明细（房型、价税、可售状态、退改规则等）。用于用户已选定具体酒店后的二次查价。
        """
        if hotelId is None and not name:
            raise Exception("hotelId 和 name 需至少提供一个")

        api_key = extract_api_key()
        params: Dict[str, Any] = {}

        if hotelId is not None:
            params["hotelId"] = hotelId
        if name:
            params["name"] = name
        if dateParam:
            params["dateParam"] = model_dump(dateParam)
        if occupancyParam:
            params["occupancyParam"] = model_dump(occupancyParam)
        if localeParam:
            params["localeParam"] = model_dump(localeParam)

        return await request_api("POST", "/hoteldetail", api_key, payload=params)
