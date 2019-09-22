# conding=utf-8
require 'rexml/document'
require 'rexml/streamlistener'
include REXML


  
class MyListener 
	include REXML::StreamListener 
	def tag_start(*args) 

		# puts "#{args.map {|x| x.inspect}.join(', ')}"
		# puts args.inspect

		# xml元素
		key_ = args.inspect.split(',')[0].split('[')[1]
		puts key_
		# 元素属性
		attribute_ = args.inspect.split(',')[1].split(']')[0]
		puts attribute_
	end

	def text(data)
		# 匹配xml数据data的文本值
		return if data =~ /^\W*$/  # whitespace only 
		# return if data =~ />([A-Za-z0-9]|[\u4e00-\u9fa5])*<\// # whitespace only 
		# abbrev = data[0..40] + (data.length > 40 ? "..." : "") 
		# xml文本值
		value_ = data.inspect
		puts value_
	end
end
  
list = MyListener.new
source = File.new "check_item.xml"
Document.parse_stream(source, list)
