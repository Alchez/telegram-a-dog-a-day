## How To

- Install docker
- Get session file for Telegram client

## Run

```bash
sudo docker run \
    -e API_ID="<API_ID>" \
    -e API_HASH="<API_HASH>" \
    -e DOGGO_API_KEY="<DOGAPI_API_KEY>" \
    -v /path/to/session/file:/usr/src/app/photo.session alchez/telegram-a-dog-a-day
```
