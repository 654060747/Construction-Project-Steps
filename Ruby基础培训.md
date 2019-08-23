# Ruby基础培训

## 1. Ruby及Rails是什么？

Ruby是一种简单的面向对象编程语言，有丰富的内置函数，可以直接在Ruby脚本中使用
Rails是一个非常富有成效的web应用框架
Ruby与Rails结合起来，形成一个ruby on rails的web开发框架

- 实例:
所有的 Ruby 文件扩展名都是 .rb
```
#!/usr/bin/ruby
a = 10
b = a
c = a + b
p c
```
上面的内容保存为 test.rb 即可运行

## 2. Rails快速创建博客系统

实现blog基本的主要三大功能：新建、修改、删除
### 新建项目：
    
    rails new blog

### 进入项目目录：

>cd blog

### 安装依赖：
>bundle install

### 生成框架：
>rails g scaffold project sn:integer title:string content:text date:date

### 将映射文件映射到数据库中
>rails db:migrate

### 启动web服务并指定端口：
>rails s -p 3002 -b 0.0.0.0

### 设置主页路径：
在 config/routes.rb 文件里, 加入：
>root "projects#index"

## 3. Rails评论表单
### 添加model
```
rails g scaffold comment project_id: integer body:text
rails db:migrate
```

## 添加对应关系
一条评论只属于一篇文章，一篇文章有多条评论，

###   修改app/models/project.rb
    has_many :comments
### 修改app/models/comment.rb
    belongs_to :project

### 修改 config/routes.rb ，添加：
    match '/projects/:id/comments', to: 'projects#comments', via: [:post]

### 修改app/views/projects/show.html.erb , 在最下面添加 显示评论 和 提交评论功能：
```
    <table class="table card-table table-vcenter text-nowrap">
        <thead>
        <tr>
        <th class="w-1">id.</th>
        <th>内容</th>
        <th>时间</th>
        </tr>
        </thead>
        <tbody>
        <% @project.comments.each do |item|  %>
        <tr>
        <td class="text-muted"><%= item.id %></td>
        <td><%= item.body %></td>
        <td><%= item.created_at %></td>
        </tr>
        <% end %>
        </tbody>
    </table>

    <form id="new_reply" action="/projects/<%= @project.id%>/comments" accept-charset="UTF-8" data-remote="true" method="post">
    <input type="hidden" name="authenticity_token" value="<%= form_authenticity_token %>">
        <div class="form-group">
        <div class="topic-editor-dropzone dz-clickable">
            <textarea class="topic-editor form-control" rows="4" tabindex="1" name="content" id="content" style="height: 100px;"></textarea>
        </div>
        </div> 
        <div class="submit-buttons">
        <button type="submit" id="reply-button" class="btn btn-primary" tabindex="2" ,="" data-disable-with="Reply">Reply</button>
        </div>
    </form>
```

### 修改app/controllers/projects_controller.rb ，添加 comments 方法：
```
  def comments
    @comment = Comment.new(project_id:params[:id], body:params[:content])
    @project = Project.find(params[:id])
    respond_to do |format|
      if @comment.save!
        format.html { redirect_to @project, notice: 'Project was successfully created.' }
        format.json { render :show, status: :created, location: @comment }
      else
        format.html { render :new }
        format.json { render json: @comment.errors, status: :unprocessable_entity }
      end
    end
  end
  ```

## 4. 添加字段
```
    rails g migration add_mail_to_projects mail:string
    rails db:migrate
```

## 5. 操作
```
    ssh ubuntu@192.168.50.xx
    cd test
```

## 7. 环境配置及实际操作问题解答

### 修改源（源也可以不更换，更换理论上下载速度更快。）：
> sudo nano /etc/apt/sources.list

### 更新一下：
> sudo apt-get update

### 自动安装最新版本：
> sudo apt install ruby

### 查看Ruby版本:
> ruby -v

### 安装libx
> sudo apt-get install libxml2-dev libxslt-dev

### 安装Rails:
> gem install rails

### 查看Rails版本：
> rails -v

### 安装 MySQL：
> sudo apt install   libsqlite3-dev    mysql-server libmysqlclient-dev
