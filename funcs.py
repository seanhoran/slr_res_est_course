def get_text_block(fname):
  # this is how to read a block of text:
  path = "..//slr_res_est_course//text_blocks"
  f = open(path + "//" + fname, "r")
  # and then write it to the app
  return f.read();
  
