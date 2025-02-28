from fastapi import Response, Depends, HTTPException, status

from app.services.long_url_service import LongUrlService


class LongUrlController:
    def __init__(self, long_url_service: LongUrlService = Depends(LongUrlService)):
        self.long_url_service = long_url_service

    def redirect_to_long_url(self, shortened_url: str) -> Response:
        long_url = self.long_url_service.get_long_url(shortened_url)

        if long_url is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return Response(
            content=long_url,
            headers={"Location": long_url},
            status_code=status.HTTP_301_MOVED_PERMANENTLY,
        )
