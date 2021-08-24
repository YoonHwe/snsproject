const clockTitle = document.querySelector(".content_dtime_clock");
function getClock() {
    const now = new Date();
    const year = String(now.getFullYear());
    let month = String(now.getMonth()).padStart(2, "0");
    const date = String(now.getDate()).padStart(2, "0");
    let hour = String(now.getHours()).padStart(2, "0");
    const minute = String(now.getMinutes()).padStart(2, "0");
    const second = String(now.getSeconds()).padStart(2, "0");
    now.setFullYear(year);
    now.setMonth(month);
    now.setDate(date);
    now.setHours(hour);
    now.setMinutes(minute);
    now.setSeconds(second);
    let day = now.getDay();
    //요일을 영어로 변환
    const dayString = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'];
    day = dayString[day-1];
    //월을 영어로 변환
    month = parseInt(month);
    const monthString = ['January','February','March','April','May','June','July','August','October','September','November','December'];
    month = monthString[month];
    //시간 변환
    hour = parseInt(hour);
    let amPm = "AM";
    if(hour >= 12){
        amPm = "PM";
    }
    if(hour == 0){
        hour = 12;
    }
    if(hour > 12){
        hour -= 12;
    }
    clockTitle.innerText = `${day}, ${month}, ${date}, ${year}, ${hour}:${minute}:${second} ${amPm}`;
}
getClock();
setInterval(getClock, 1000);
