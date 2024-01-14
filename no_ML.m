clear,clc

dataset = "f_analysis\FFT=2^14";
dirOutput = dir(fullfile(dataset, '*.txt'));
filenames = {dirOutput.name};
random_files = filenames(randperm(numel(filenames), numel(filenames)));
cnt = [0 0 0 0 0 0 0 0 0 0 0];
correct = [0 0 0 0 0 0 0 0 0 0 0];
for i=1:length(random_files)
    fprintf("Testing progress: %d/%d\n", i,length(random_files));
    sig = importdata(fullfile(dataset, random_files(i)));

%     Testing...
    [peak1, index1] = max(sig(find_index(6000):find_index(8000)));
    [peak2, index2] = max(sig(find_index(4000):find_index(5000)));
    [peak3, index3] = max(sig(find_index(5000):find_index(6000)));
    [peak4, index4] = max(sig(1:find_index(5000)));
    [peak5, index5] = max(sig(find_index(2370):find_index(2680)));
%     find_index(6500)
    index1 = index1+find_index(6000);
    index2 = index2+find_index(4000);
    predict = 0;
    if peak4 > 6 % 800
        predict = 800;
    elseif peak4 > 1.75 % 400
        predict = 400;
    else
        if peak2 > 0.75 % 1200
            predict = 1200;
        elseif peak3 > 0.5 % 1600
            predict = 1600;
        else
            if index1 > find_index(6600) && index1 < find_index(6800) && peak1 < 0.445 % 2000
                predict = 2000;
            end
            if index1 > find_index(6600) && index1 < find_index(6800) && peak1 > 0.445 % 2400
                predict = 2400;
            end
            if index1 > find_index(6800) && index1 < find_index(6950) % 2800
                predict = 2800;
            end
            if index1 > find_index(6950) && index1 < find_index(7300) % 3200
                predict = 3200;
            end
            if index1 > find_index(7300) % 3600-4000
                if peak5 < 1.1
                    predict = 3600;
                else
                    predict = 4000;
                end
            end
        end
    end
    
%     if index1 > find_index(7575) % 4000
%         predict = 4000;
%     end
    cnt(11) = cnt(11)+1;

    temp = split(random_files(i),'raw');
    gt = str2double(temp(1));
    cnt(gt/400) = cnt(gt/400)+1;

%     Test accuracy
    if predict == gt
        correct(11) = correct(11)+1;
        correct(gt/400) = correct(gt/400)+1;
    end
end

for i=1:10
    fprintf("The accuracy of degree of tightness %d is %f%%\n", i*400, eval(num2str(correct(i)/cnt(i)*100)));
end
fprintf("The accuracy of this model is %f%%\n", eval(num2str(correct(11)/cnt(11)*100)));

% Find the index of "freq"(Hz) with respect to the frequency spectrum
function index = find_index(freq)
    sampling_rate = 51.2*1e3;
    fft_size = 2^14;
    index = floor(freq/(sampling_rate/2)*(idivide(fft_size,int32(2),"floor")+1));
    if index < 1
        index = 1;
    end
end