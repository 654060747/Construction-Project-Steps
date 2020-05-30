## 根据总时长截取
```
ffmpeg -ss 视频截取开始时间 -i input.mp4  -c copy -t 需要截取的总时间 output.mp4
ffmpeg -ss 视频截取开始时间 -i input.mp4 -t 需要截取的总时间 -c copy output.mp4
```

## 结束时间建议多1秒,剪切时间不精准,-y有同名文件不提示直接覆盖
```
ffmpeg  -i 源文件名 -vcodec copy -acodec copy -ss 视频截取开始时间 -to 视频截取结束时间 目标文件名 -y
```

## accurate_seek剪切时间更加精确,accurate_seek必须放在-i参数之前（非重新编码，快）
```
ffmpeg -ss 开始时间 -to 结束时间 -accurate_seek -i test.mp4 -codec copy cut.mp4
```
## 如果编码格式采用的copy 最好加上 -avoid_negative_ts 1参数（非重新编码，快）
```
ffmpeg -ss 开始时间 -to 结束时间 -accurate_seek -i test.mp4 -codec copy -avoid_negative_ts 1 cut.mp4
ffmpeg -ss 开始时间 -t 总时长 -accurate_seek -i test.mp4 -codec copy -avoid_negative_ts 1 cut.mp4
```
## 重新编码进行剪切（目前找到最精准剪切，比较慢）
```
ffmpeg -ss [start] -t [duration] -i [in].mp4  -c:v libx264 -c:a aac -strict experimental -b:a 98k [out].mp4
```
