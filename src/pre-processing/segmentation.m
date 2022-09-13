clc;    
close all;  
clearvars;
workspace;  
format long g;
format compact;
fontSize = 16;
fprintf('Beginning to run %s.m ...\n', mfilename);
%-----------------------------------------------------------------------------------------------------------------------------------
% Read in image.
folder = [];
baseFileName = 'C:/Users/User/Documents/research/researchArea/dataset/removal/altissimum/51.png';
fullFileName = fullfile(folder, baseFileName);
if ~exist(fullFileName, 'file')
	fullFileNameOnSearchPath = baseFileName; 
	if ~exist(fullFileNameOnSearchPath, 'file')
		errorMessage = sprintf('Error: %s does not exist in the search path folders.', fullFileName);
		uiwait(warndlg(errorMessage));
		return;
	end
end
% It's not an RGB image!  It's an indexed image, so read in the indexed image...
rgbImage = imread(fullFileName);
[rows, columns, numberOfColorChannels] = size(rgbImage)
% Display the test image.
subplot(2, 2, 1);
imshow(rgbImage, []);
axis('on', 'image');
caption = sprintf('Image : "%s"', baseFileName);
title(caption, 'FontSize', fontSize, 'Interpreter', 'None');
drawnow;
hp = impixelinfo(); % Set up status line to see values when you mouse over the image.
% Set up figure properties:
% Enlarge figure to full screen.
hFig1 = gcf;
hFig1.Units = 'Normalized';
hFig1.WindowState = 'maximized';
% Get rid of tool bar and pulldown menus that are along top of figure.
% set(gcf, 'Toolbar', 'none', 'Menu', 'none');
% Give a name to the title bar.
hFig1.Name = 'Demo by Image Analyst';
mask = imread('C:/Users/User/Documents/research/researchArea/dataset/removal/altissimum/51.png');
[rowsm, columnsm, numberOfColorChannelsm] = size(mask)
mask = mask(:,:,1) > 128; % Convert to binary.
if rows ~= rowsm || columns ~= columnsm
	% Resize mask to match image.
	mask = imresize(mask, [rows, columns], 'Nearest');
end
% Display the initial mask image.
subplot(2, 2, 2);
imshow(mask, []);
hp = impixelinfo(); % Set up status line to see values when you mouse over the image.
axis('on', 'image');
title('Mask', 'FontSize', fontSize, 'Interpreter', 'None');
drawnow;
% Mask the image using bsxfun() function to multiply the mask by each channel individually.  Works for gray scale as well as RGB Color images.
maskedRgbImage = bsxfun(@times, rgbImage, cast(mask, 'like', rgbImage));
% Display the final masked image.
subplot(2, 2, 3);
imshow(maskedRgbImage, []);
axis('on', 'image');
title('Masked Image', 'FontSize', fontSize, 'Interpreter', 'None');
drawnow;
hp = impixelinfo(); 
backgroundImage = bsxfun(@times, rgbImage, cast(~mask, 'like', rgbImage));
subplot(2, 2, 4);
imshow(backgroundImage, []);
axis('on', 'image');
title('Background Image', 'FontSize', fontSize, 'Interpreter', 'None');
drawnow;
hp = impixelinfo()