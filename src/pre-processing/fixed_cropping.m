close all;
I=imread('C:/Users/User/Desktop/seed/anticlinal/1.png');
output_folder='Desktop/c'
figure, imshow(I);
I=rgb2gray(I);
figure, imshow(I);
%BW=I<100;
T=adaptthresh(I, 0.6)
figure, imshow(T)
%T=graythresh(I)
BW=imbinarize(I, T)
figure,imshow(BW);
labeledImage = bwlabel(BW);
figure,imshow(labeledImage);

measurements = regionprops(labeledImage, 'BoundingBox', 'Area');


for k = 1 : length(measurements)%detect boundary box of current rectangle
thisBB = measurements(k).BoundingBox;
%disp(thisBB)
I2=imcrop(I,[thisBB(1),thisBB(2),thisBB(3),thisBB(4)]);%I2 is a cropped image with the corresponding bbs xmin, ymin,heigth,width--that specifies the size and position of the crop rectangle.
[rows cols depth]=size(I2);%number of output dimensions

if rows*cols>400    
%if (rows>300) && (cols>300)
    %figure,imshow(I2);
    %outputFileName = fullfile(output_folder, '.png' ); %['alexianum_' num2str(k) '.png']
    %imwrite(I2, outputFileName);
 %end
end
end
