### latest models

pleias3b_q4 https://drive.google.com/file/d/1JGmJZVkZKIfH-yYWo7K4xgLX9LFL-IPu/view?usp=drive_link
pleias350M https://drive.google.com/file/d/1PgFKgLmSdRGKNcX8EhqlThbrbo4gO_G8/view?usp=sharing

### Run the code

To run the code you need llamafile running on the background, or get response key changed to debug mode. It is on debug mode by defailt now
```bash
./Llama-3.2-1B-Instruct.Q6_K.llamafile --server --nobrowser -n 20
python -m src.main
```
You can download the model [there](https://huggingface.co/Mozilla/Llama-3.2-1B-Instruct-llamafile/blob/main/Llama-3.2-1B-Instruct.Q6_K.llamafile)

[//]: # (Usful links for implemetation )
[//]: # (https://thepythoncode.com/article/make-pdf-viewer-with-tktinter-in-python)

### To launch PyQt designer:
1. Install PyQt and Qt
On conda:
```bash
conda install pyqt qt
```

2. Launch the designer
```bash
designer
```
