%%Data loading
sw_vel = importdata('smartwatch_vell.log');
ids = str2num(cell2mat(sw_vel.textdata(:,1)));
yarp_time = str2num(cell2mat(sw_vel.textdata(:,2)));
sw_vel = [ids, yarp_time, sw_vel.data];
%%Time conversion
sw_vel(:,6) = sw_vel(:,6)./1000; 
delta_time = flip([0; cumsum(diff(sw_vel(:,6)))]);
sw_vel(:,7) = sw_vel(end,2) - delta_time;
%%Final Dataset
smartwatch_vel = [sw_vel(:,7),sw_vel(:,3:5)];

%%Plotting
subplot(3,1,1);
plot(smartwatch_vel(:,1), smartwatch_vel(:,2))
subplot(3,1,2);
plot(smartwatch_vel(:,1), smartwatch_vel(:,3))
subplot(3,1,3);
plot(smartwatch_vel(:,1), smartwatch_vel(:,4))

%%Data loading
sw_acc = importdata('smartwatch_acc.log');
ids = str2num(cell2mat(sw_acc.textdata(:,1)));
yarp_time = str2num(cell2mat(sw_acc.textdata(:,2)));
sw_acc = [ids, yarp_time, sw_acc.data];
%%Time conversion
sw_acc(:,6) = sw_acc(:,6)./1000; 
delta_time = flip([0; cumsum(diff(sw_acc(:,6)))]);
sw_acc(:,7) = sw_acc(end,2) - delta_time;
%%Final Dataset
smartwatch_acc = [sw_acc(:,7),sw_acc(:,3:5)];

%%Plotting
subplot(3,1,1);
plot(smartwatch_acc(:,1), smartwatch_acc(:,2))
subplot(3,1,2);
plot(smartwatch_acc(:,1), smartwatch_acc(:,3))
subplot(3,1,3);
plot(smartwatch_acc(:,1), smartwatch_acc(:,4))

