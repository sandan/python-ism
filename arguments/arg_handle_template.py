import argparse

if __name__ == '__main__':
  description = "parse\
                 some more things"
  p = argparse.ArgumentParser(description="parse some things."+description)

  p.add_argument("type", help="type of plot to generate. Only pandas supported plots are used for now.")
  p.add_argument("title", help="a title for the generated plot")
  p.add_argument("-xl","--xlabel", help="optional x axis label", nargs="?")
  p.add_argument("-yl","--ylabel", help="optional y axis label", nargs="?")
  p.add_argument("-x", "--xcol", help="The x column. If not specified a non-negative integer column is used.", nargs="?")
  p.add_argument("-ys", "--ycols",  help="the y columns", nargs="+")
  p.add_argument("-c", "--cols",  help="the names in the select clause (specified in the same order)", nargs="+")

  opts = vars(p.parse_args())
  print(opts)

