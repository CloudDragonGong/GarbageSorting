# GarbageSorting（垃圾分类识别服务）

一个基于 **Flask + YOLOv8** 的垃圾分类识别项目，支持：
- 上传单张图片进行目标检测与垃圾类别识别。
- 返回标注后的图片下载地址与类别结果。
- 提供简单前端页面用于演示调用。

## 1. 项目功能

- **单图识别接口**：`POST /img_upload/single`
- **识别结果图片下载**：`GET /img_download/<filename>`
- **演示页面**：`GET /demo`
- **模板页面**：`GET /sort`

当前类别（TrashNet 六分类）：
- cardboard
- glass
- metal
- paper
- plastic
- trash

并映射为是否可回收：
- `yes`：metal / paper / glass / cardboard / plastic
- `no`：trash

## 2. 项目结构

```text
GarbageSorting/
├── main.py                     # Flask 应用入口
├── model/YOLO_classifier.py    # YOLO 模型封装（图片/视频）
├── service/img_worker.py       # 业务调度层
├── server/server.py            # 路由与接口实现
├── server/response.py          # 统一响应格式
├── conf/config_parse.py        # 配置解析
├── configs/config.ini          # 默认配置
├── models/best.pt              # 训练好的权重（默认）
├── imgs/                       # 上传与输出图片目录（默认）
├── templates/                  # 模板页面
├── static/                     # 静态资源
└── requirements.txt            # 依赖列表
```

## 3. 环境要求

- Python 3.9+（建议）
- 支持 `torch` 与 `ultralytics` 运行环境
- 建议使用虚拟环境（venv / conda）

## 4. 安装与启动

### 4.1 安装依赖

```bash
pip install -r requirements.txt
```

### 4.2 配置文件

项目通过 `-c` 参数传入配置文件路径，例如：`configs/config.ini`。

示例：

```ini
[machine]
ip = 0.0.0.0
port = 17304

[img_path]
upload_folder = ./imgs
download_folder = ./imgs

[models]
model_path= ./models/best.pt

[external]
ip = 39.107.107.212

[setting]
debug_mode = false
```

### 4.3 启动服务

```bash
python main.py -c configs/config.ini
```

## 5. 接口说明

### 5.1 上传并识别单张图片

- **URL**：`POST /img_upload/single`
- **Content-Type**：`multipart/form-data`
- **字段**：`img`（文件）

返回示例：

```json
{
  "code": 200,
  "message": "ok",
  "data": {
    "image_url": "/img_download/output_xxx.png",
    "type": {
      "plastic": "yes",
      "trash": "no"
    }
  }
}
```

### 5.2 下载结果图

- **URL**：`GET /img_download/<filename>`
- **说明**：返回识别后带标注图片。

## 6. 前端页面

- `GET /demo`：返回静态演示页面（`static/demo2.html`）。
- `GET /sort`：返回模板页面（`templates/pictureDivision.html`），支持 `server_url` 查询参数。

## 7. 数据与模型来源

- 数据集（TrashNet）：<https://github.com/garythung/trashnet>
- YOLO（Ultralytics）：<https://github.com/ultralytics/ultralytics>
- 参考流程文章：<https://zhuanlan.zhihu.com/p/624244160>

## 8. 常见问题

1. **启动报 config not found**
   - 请确认已使用 `-c` 指定配置文件，且路径正确。

2. **模型加载失败**
   - 请检查 `model_path` 是否存在，并确认 `torch/ultralytics` 安装成功。

3. **上传成功但无结果图**
   - 检查 `upload_folder`、`download_folder` 是否有写权限。

## 9. 后续可优化方向

- 增加批量图片与视频接口。
- 补充接口鉴权、限流与日志追踪。
- 优化异常处理与错误码体系。
- 提供 Dockerfile 与一键部署脚本。
