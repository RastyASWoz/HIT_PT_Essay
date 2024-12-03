// 包依赖：OpenCvSharp4 OpenCvSharp4.runtime.win
using OpenCvSharp;

Mat src1 = new Mat(@"Baboon.bmp", ImreadModes.AnyColor);
Mat dst1 = new Mat();
Mat dst2 = new Mat();
//Cv2.GaussianBlur(src1, dst1, new Size(3, 3), 10.1, 11.0);
Cv2.GaussianBlur(src1,dst2, new Size(5, 5), 10.1);
// 将图像保存到文件
dst1.ImWrite(@"Baboon_out1.bmp");
dst2.ImWrite(@"Baboon_out2.bmp");

Mat src2 = new Mat(@"Peppers.bmp", ImreadModes.AnyColor);
Mat dst3 = new Mat();
Mat dst4 = new Mat();
//Cv2.GaussianBlur(src2, dst3, new Size(3, 3), 5);
Cv2.GaussianBlur(src2, dst4, new Size(5, 5), 15);
// 将图像保存到文件
dst3.ImWrite(@"Peppers_out1.bmp");
dst4.ImWrite(@"Peppers_out2.bmp");