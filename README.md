# 缘分测算器

一个 Vue 3 + FastAPI 的姓名缘分测算小应用。前端是粉色系现代风格，支持两个人的姓名和出生日期输入，后端返回 0-100 分、分数文案和三个参考维度。

## 功能

- 姓名缘分测算
- 支持可选出生日期
- 0-100 分评分
- 从 `data/level.yaml` 读取对应文案
- 简洁的加载态与结果面板

## 本地开发

先安装依赖：

```bash
pip install -r requirements.txt
cd frontend
npm install
```

后端默认端口：`13144`

前端开发端口：`5173`

### Windows

在项目根目录运行：

```bash
python run.py
```

如果你只想单独启动后端：

```bash
python -m uvicorn backend.main:app --app-dir F:\cmyf\Desktop\yuan --host 127.0.0.1 --port 13144
```

如果你只想单独启动前端：

```bash
npm --prefix F:\cmyf\Desktop\yuan\frontend run dev -- --host 127.0.0.1
```

### Linux

先进入你的 Python 环境并安装依赖：

```bash
pip install -r requirements.txt
cd frontend
npm install
```

单独启动后端：

```bash
python -m uvicorn backend.main:app --app-dir /path/to/yuan --host 0.0.0.0 --port 13144
```

单独启动前端：

```bash
npm --prefix /path/to/yuan/frontend run dev -- --host 0.0.0.0
```

使用 `nohup` 后台部署后端：

```bash
nohup python -m uvicorn backend.main:app --app-dir /path/to/yuan --host 0.0.0.0 --port 13144 > backend.log 2>&1 &
echo $! > backend.pid
```

## Linux 部署脚本

把脚本放在 `scripts/` 目录下后，先赋予执行权限：

```bash
chmod +x scripts/restart.sh scripts/stop.sh
```

启动或重启后端：

```bash
./scripts/restart.sh
```

停止后端：

```bash
./scripts/stop.sh
```

## Windows 部署脚本

直接双击或在命令行里运行：

```bat
scripts\\restart.bat
scripts\\stop.bat
```

## 接口

后端健康检查：

```text
GET http://127.0.0.1:13144/api/health
```

缘分测算接口：

```text
POST http://127.0.0.1:13144/api/compatibility
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

## 说明

- 前端默认请求地址是 `http://yuan.voyagers.work/api`
- 如果你部署到别的机器，可以通过环境变量 `VITE_API_URL` 覆盖前端请求地址
