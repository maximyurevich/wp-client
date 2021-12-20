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
                                "title": "Test",
                                "content": "Test",
                                "status": "publish"
                            }
                        ),

                    wp_client.patch(client, endpoint=4, payload = {
                        "title": "Hello",
                    }),
                    wp_client.patch(client, endpoint=4,
                        payload =
                            {
                                "title": "Test",
                                "content": "Test",
                                "status": "publish"
                            }
                        ),
                )

    asyncio.run(main())
