# 缘分测算器

一个 Vue 3 + FastAPI 的姓名缘分测算小应用。前端提供粉色系现代测算页面，后端根据两个人的姓名和可选出生日期返回 0-100 分、分数文案和三个缘分维度。

## 安装依赖

```bash
pip install -r requirements.txt
cd frontend
npm install
```

## 启动

```bash
conda run -n uc python run.py
```

也可以分别启动：

```bash
conda run -n uc python -m uvicorn backend.main:app --app-dir F:\cmyf\Desktop\yuan --host 127.0.0.1 --port 8000
npm --prefix F:\cmyf\Desktop\yuan\frontend run dev -- --host 127.0.0.1
```

前端地址：

```text
http://127.0.0.1:5173
```

后端接口：

```text
POST http://127.0.0.1:8000/compatibility
```

请求示例：

```json
{
  "name1": "张三",
  "birthday1": "1999-01-01",
  "name2": "李四",
  "birthday2": "2000-02-02"
}
```
