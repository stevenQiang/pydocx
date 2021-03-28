## PyDocX

公司目前有几个协议需要从docx转成html，放到app上面；网上找了一圈，只有这个包 [PyDocX](<https://github.com/CenterForOpenScience/pydocx>) 导出来的样式有点适合，但还有点不太一样，所以fork下来，
稍微修改了一下，以达到想要的效果。最终效果见test.html，原docx文件见test.docx.


## 使用

```
pip install -r requirements/docs.txt -r requirements/testing.txt
python run.py
```

