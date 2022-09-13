clc;    % Clear the command window.
close all;  % Close all figures (except those of imtool.)
clear;  % Erase all existing variables. Or clearvars if you want.
workspace;  % Make sure the workspace panel is showing.
format long g;
format compact;
fontSize = 20;
%===============================================================================
% Read in gray scale demo image.
folder = 'C:/Users/User/Desktop/seed/periclinal/big_verruca/'; % Determine where demo folder is (works with all versions).
baseFileName = 'crop_76.png';
% Get the full filename, with path prepended.
fullFileName = fullfile(folder, baseFileName);
% Check if file exists.
if ~exist(fullFileName, 'file')
  % The file doesn't exist -- didn't find it there in that folder.
  % Check the entire search path (other folders) for the file by stripping off the folder.
  fullFileNameOnSearchPath = baseFileName; % No path this time.
  if ~exist(fullFileNameOnSearchPath, 'file')
    % Still didn't find it.  Alert user.
    errorMessage = sprintf('Error: %s does not exist in the search path folders.', fullFileName);
    uiwait(warndlg(errorMessage));
    return;
  end
end
rgbImage = imread(fullFileName);
% Display the image.
subplot(2, 2, 1);
imshow(rgbImage, []);
title('Original Image', 'FontSize', fontSize, 'Interpreter', 'None');
axis('on', 'image');
hp = impixelinfo();
% Get the dimensions of the image.
% numberOfColorChannels should be = 1 for a gray scale image, and 3 for an RGB color image.
[rows, columns, numberOfColorChannels] = size(rgbImage)
if numberOfColorChannels > 1
  % It's not really gray scale like we expected - it's color.
  % Use weighted sum of ALL channels to create a gray scale image.
  %     grayImage = rgb2gray(rgbImage);
  % ALTERNATE METHOD: Convert it to gray scale by taking only the green channel,
  % which in a typical snapshot will be the least noisy channel.
  grayImage = rgbImage(:, :, 3); % Take green channel. %2
else
  grayImage = rgbImage; % It's already gray scale.
end
% Now it's gray scale with range of 0 to 255.
% Display the histogram of the image.
subplot(2, 2, 2);
[counts, binLocations] = imhist(grayImage);
% Suppress bin 1 because it's so tall
counts(1) = 0;
bar(binLocations, counts);
grid on;
title('Histogram of Image', 'FontSize', fontSize, 'Interpreter', 'None');
%------------------------------------------------------------------------------
% Set up figure properties:
% Enlarge figure to full screen.
set(gcf, 'Units', 'Normalized', 'OuterPosition', [0, 0.04, 1, 0.96]);
% Get rid of tool bar and pulldown menus that are along top of figure.
% set(gcf, 'Toolbar', 'none', 'Menu', 'none');
% Give a name to the title bar.
set(gcf, 'Name', 'Demo by ImageAnalyst', 'NumberTitle', 'Off')
drawnow;
% Binarize the image
% Get the mask where the region is solid.
binaryImage = grayImage > 55 
% Fill it and take the largest blob:
binaryImage = imfill(binaryImage, 'holes');
binaryImage = bwareafilt(binaryImage, 1);
% Display the image.
subplot(2, 2, 3);
imshow(binaryImage, []);
title('Initial Binary Image', 'FontSize', fontSize, 'Interpreter', 'None');
axis('on', 'image');
hp = impixelinfo();
drawnow;
% Use it to mask the original image.
finalImage = grayImage; % Initialize
finalImage(~binaryImage) = 0; % Erase outside the mask.
% Display the image.
subplot(2, 2, 4);
imshow(finalImage, []);
title('Final, Masked Image', 'FontSize', fontSize, 'Interpreter', 'None');
axis('on', 'image');
hp = impixelinfo();
















