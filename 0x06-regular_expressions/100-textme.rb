#!/usr/bin/env ruby
puts ARGV[0].scan(/\[From:(.*?)\]\n\[to:(.*?)\]\[flags:(.*?)\]/).join()
