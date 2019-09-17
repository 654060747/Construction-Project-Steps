require 'rexml/document'
require 'rexml/streamlistener'
include REXML


  
class MyListener 
 include REXML::StreamListener 
 def tag_start(*args) 
 puts "#{args.map {|x| x.inspect}.join(', ')}"
 end
  
 def text(data) 
 # return if data =~ /^\w*$/  # whitespace only 
 # return if data =~ />([A-Za-z0-9]|[\u4e00-\u9fa5])*<\// # whitespace only 
 return if data =~ />.<\// # whitespace only 
 # abbrev = data[0..40] + (data.length > 40 ? "..." : "") 
 puts " text : #{data.inspect}"
 end
end
  
list = MyListener.new
source = File.new "check_item.xml"
Document.parse_stream(source, list)
