alias mly_build='docker build -t mly .'
# use `pwd` to specify the current directory (inside mly project folder)
# use %CD% if you are in windows
# reference: https://github.com/moby/moby/issues/4830#issuecomment-264366876
alias mly_run='docker run -i -t -v `pwd`:/mly mly'
