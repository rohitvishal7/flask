package service;

import service.support.MyDate;


public class DateDifferenceProvider {
	
	
	private static final int FEB = 2;
	private static final int DAY_IN_A_LEAP_YEAR = 366;
	private static final int DAY_IN_A_NON_LEAP_YEAR = 365;
	private static int Day_IN_JAN=31;
	private static int Day_IN_FEB=28;
	private static int Day_IN_MAR=31;
	private static int Day_IN_APR=30;
	private static int Day_IN_MAY=31;
	private static int Day_IN_JUN=30;
	private static int Day_IN_JUL=31;
	private static int Day_IN_AUG=31;
	private static int Day_IN_SEP=30;
	private static int Day_IN_OCT=31;
	private static int Day_IN_NOV=30;
	private static int Day_IN_DEC=31;
	
	
	
	public static int daysInMonth[]= {Day_IN_JAN,
		Day_IN_FEB,
		Day_IN_MAR,
		Day_IN_APR,
		Day_IN_MAY,
		Day_IN_JUN,
		Day_IN_JUL,
		Day_IN_AUG,
		Day_IN_SEP,
		Day_IN_OCT,
		Day_IN_NOV,
		Day_IN_DEC};
	
	public static long getDateDifference (MyDate startDate, MyDate endDate)
	{
		if (sameDate(startDate, endDate)&&
				sameMonth(startDate, endDate)&&
				sameYear(startDate, endDate))
		{
			return 0;
		}
		else if(sameYear(startDate, endDate)&& 
				sameMonth(startDate, endDate))
		{
			return endDate.getDd()- startDate.getDd(); 
		}
			
		else if(sameYear(startDate, endDate) &&
				!sameMonth(startDate, endDate))
		{	
			return remainingDaysInMonth(startDate)+
					daysInIntervingMonth(startDate, endDate)+
					leadingMonth(endDate);
		}
		else
		{
			return remainingDaysInYear(startDate)+
					leadingYear(endDate)+
					daysInInterveningYear(startDate, endDate);
		}
		
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	private static boolean sameYear(MyDate date1, MyDate date2){
		
		return(date1.getYyyy()==date2.getYyyy());
	}
	
	private static boolean sameMonth(MyDate date1, MyDate date2){
		
		return(date1.getMm()==date2.getMm());
	}
	
	private static boolean sameDate(MyDate date1, MyDate date2){
		
		return(date1.getDd()==date2.getDd());
	}
	
	private static long remainingDaysInMonth(MyDate date){
		int remainingDays;
		int month=date.getMm();
		remainingDays= daysInMonth[month-1]-date.getDd();
		if(isLeapYear(date)&& isFebruary(date))
			remainingDays++;
		return remainingDays;
	}
	
	private static long leadingMonth(MyDate date)
	{
		return date.getDd();
	}
	
	private static boolean isFebruary(MyDate date) {
		int month=date.getMm();
		if(month==FEB){
			return true;
		}
		return false;
	}

	private static boolean isLeapYear(MyDate date) {
		int year=date.getYyyy();
		if((year%400) ==0 || year%4==0 && year%100!=0)
		return true;
		else
		return false;
	}
	

	private static long daysInIntervingMonth(MyDate startDate, MyDate endDate){
		int startMonth=startDate.getMm();
		int endMonth=endDate.getMm();
		int days=0;
			
		for(int month=startMonth+1; month <endMonth; month++)
		{
			if(isLeapYear(startDate)&& month==FEB){
				++days;
				
			}
			days=days+daysInMonth[month-1];
		}
	
		return days;
	}
	
	private static int daysInInterveningYear(MyDate startDate, MyDate endDate) {
		
		int remainingdays =0;
		
		for(int year = startDate.getYyyy()+1; year<endDate.getYyyy(); year++)
		{
			if(isLeapYear(new MyDate(1,1,year)))
				remainingdays = remainingdays + DAY_IN_A_LEAP_YEAR;
			else
				remainingdays = remainingdays + DAY_IN_A_NON_LEAP_YEAR;
		}		
		
		return remainingdays;
	}
	
	private static long remainingDaysInYear(MyDate startDate) {
		
		int daysRemaining =0;
		
		for(int month = startDate.getMm()+1; month <= 12; month++)
		{
			daysRemaining = daysRemaining + daysInMonth[month-1];
		}
		
		daysRemaining = daysRemaining + (daysInMonth[startDate.getMm()-1]-startDate.getDd());
		
		if(isLeapYear(startDate) && startDate.getMm()>=FEB)
			daysRemaining++;
		
		return daysRemaining;
		
	}


	private static long leadingYear(MyDate endDate) {
		
		int daysRemaining =0;
		
		for(int month = 1; month < endDate.getMm(); month++)
		{
			daysRemaining = daysRemaining + daysInMonth[month-1];
		}
		
		daysRemaining = daysRemaining + endDate.getDd();
		
		if(isLeapYear(endDate) && endDate.getMm()>=FEB)
			daysRemaining++;
		
		return daysRemaining;
	}



}
