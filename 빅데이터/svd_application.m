img = imread('figure1.jpg');
imshow(img);

grayimg = rgb2gray(img);

imshow(grayimg);

[numRows,numCols] = size(grayimg);
[U,S,V] = svd(double(grayimg));

%%% 64
num_sing_vectors = 64;

S(num_sing_vectors+1:numRows,num_sing_vectors+1:numCols) = 0;

VT = V';
outputimg = U(:,1:num_sing_vectors)*S(1:num_sing_vectors,1:num_sing_vectors)*VT(1:num_sing_vectors,:);
outputimg64 = cast(outputimg,'uint8');

%%% 32
num_sing_vectors = 32;

S(num_sing_vectors+1:numRows,num_sing_vectors+1:numCols) = 0;

VT = V';
outputimg = U(:,1:num_sing_vectors)*S(1:num_sing_vectors,1:num_sing_vectors)*VT(1:num_sing_vectors,:);
outputimg32 = cast(outputimg,'uint8');

%%% 16
num_sing_vectors = 16;

S(num_sing_vectors+1:numRows,num_sing_vectors+1:numCols) = 0;

VT = V';
outputimg = U(:,1:num_sing_vectors)*S(1:num_sing_vectors,1:num_sing_vectors)*VT(1:num_sing_vectors,:);
outputimg16 = cast(outputimg,'uint8');


subplot(2,2,1), imshow(grayimg);
subplot(2,2,2), imshow(outputimg16);
subplot(2,2,3), imshow(outputimg32);
subplot(2,2,4), imshow(outputimg64);