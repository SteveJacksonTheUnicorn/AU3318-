clear,clc

sampling_rate = 51.2*1e3;
fft_size = 2^14;
nums = [35 43 32 34 37 42 31 33 43 52];
names = [400 800 1200 1600 2000 2400 2800 3200 3600 4000];

fs = 0:(sampling_rate/2)/(fft_size/2+1):sampling_rate/2; %横坐标
fs = fs(1:length(fs)-1);

for i=1:10
    i
    data = importdata(fullfile('f_analysis_average/FFT=2^14/', [num2str(names(i)), 'raw.txt'])); %纵坐标
    subplot("Position",[0.05,0.9-0.089*(i-1),0.84,0.05]);
    plot(fs, data, "b");
    set(gca,'FontSize',6);
    title("松紧度为"+names(i)+"时的共"+nums(i)+"幅 单侧幅值频谱平均值")
end