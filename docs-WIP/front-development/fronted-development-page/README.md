---
description: >-
  This page is used for describing details of application development, cross
  platform integration etc
---

# Fronted development page

Seems like we have decided to build an app using FastHTML&#x20;

I will list usful links:

[https://gallery.fastht.ml/widgets/pdf/display/](https://gallery.fastht.ml/widgets/pdf/display/) -- example with pdf display, might be useful for our app&#x20;

Working examples for uploading files&#x20;

```python
from fastapi import FastAPI, UploadFile, HTTPException, status
from fastapi.responses import HTMLResponse
from typing import List
import aiofiles

app = FastAPI()


@app.post('/upload')
async def upload(files: List[UploadFile]):
    for file in files:
        try:
            contents = await file.read()
            async with aiofiles.open(file.filename, 'wb') as f:
                await f.write(contents)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='There was an error uploading the file(s)',
            )
        finally:
            await file.close()

    return {'message': f'Successfuly uploaded {[file.filename for file in files]}'}


# Access the form at 'http://127.0.0.1:8000/' from your browser
@app.get('/')
async def main():
    content = '''
    <body>
    <form action='/upload' enctype='multipart/form-data' method='post'>
    <input name='files' type='file' multiple>
    <input type='submit'>
    </form>
    </body>
    '''
    return HTMLResponse(content=content)



```

