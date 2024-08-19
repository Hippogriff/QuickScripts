ffmpeg -framerate 20 -i rgb_test_baking_new_video_16384_False_%04d_white.png -vf rotate=PI/2 -vb 40M -c:v libx264 -r 30 -pix_fmt yuv420p rgb_test_baking_new_video_16384_False_white.mp4
