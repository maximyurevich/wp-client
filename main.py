"""Main file for the project"""
import asyncio
import os
import aiohttp
from dotenv import load_dotenv

from wordpress_client import WordpressRestApiClient

load_dotenv()

if __name__ == "__main__":
    async def main():
        """Main function"""
        async with aiohttp.ClientSession() as client:
            if os.environ:
                wp_client = WordpressRestApiClient(
                    os.environ.get("URL"),
                    os.environ.get("WP_USER"),
                    os.environ.get("WP_PASS")
                )

                await asyncio.gather(
                    wp_client.get(client, endpoint = 2),
                    wp_client.delete(client, endpoint = 3),
                    wp_client.get(client),
                    wp_client.post(client,
                        payload =
                            {
                                "title": "Lorem Ipsum",
                                "content": "Lorem ipsum sit amet",
                                "status": "publish"
                            }
                        ),

                    wp_client.patch(client, endpoint=4, payload = {
                        "title": "Съешь ещё этих мягких французских булок",
                    }),
                    wp_client.put(client, endpoint=4,
                        payload =
                            {
                                "title": "съешь ещё этих мягких французских булок",
                                "content": "Да выпей чаю",
                                "status": "publish"
                            }
                        ),
                )

    asyncio.run(main())
