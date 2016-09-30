package test;

import service.DateDifferenceProvider;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import service.support.MyDate;


public class TestUnit {

	
	public static void main(String[] args) {
     

                
                ArrayList<MyDateTestRecord> testData= new ArrayList<MyDateTestRecord>();
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case1
                                                new MyDate(06, 04, 2011),
                                                0));
                
                
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case2
                                                new MyDate(18, 04, 2011),
                                                12));
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case3
                                                new MyDate(18, 05, 2011),
                                                42));
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case4
                                                new MyDate(18, 06, 2011),
                                                73));
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case5
                                                new MyDate(18, 12, 2011),
                                                256));
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case6
                                                new MyDate(18, 12, 2012),
                                                622));
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case7
                                                new MyDate(18, 12, 2013),
                                                987));
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case8
                                                new MyDate(18, 12, 2113),
                                                37511));
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case9
                                                new MyDate(18, 12, 2413),
                                                147084));
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 04, 2011),//case10
                                                new MyDate(18, 12, 2813),
                                                293181));
                testData.add(
                                new MyDateTestRecord(
                                                new MyDate(06, 01, 2011),//case11
                                                new MyDate(06, 03, 2011),
                                                59));
                testData.add(
                                new MyDateTestRecord(new MyDate(06, 01, 2012),//case12
                                                new MyDate(06, 03, 2012),
                                                60));
                
                testData.add(
                                new MyDateTestRecord(new MyDate(06, 02, 2012),//case13
                                                new MyDate(06, 03, 2012),
                                                29));
                testData.add(
                                new MyDateTestRecord(new MyDate(22, 01, 2012),//case14
                                                new MyDate(15, 11, 2012),
                                                298));
                testData.add(
                                new MyDateTestRecord(new MyDate(6, 2, 2012),//case15
                                                new MyDate(6, 12, 2012),
                                                304));
                
                
                for(MyDateTestRecord testCase : testData){
                        
                        MyDate startDate=testCase.startDate;
                        MyDate endDate=testCase.endDate;
                        long expectedResult =testCase.expectedResult;
                        long obtainedResult = DateDifferenceProvider.getDateDifference(startDate, endDate);
                        
                           if(expectedResult== obtainedResult)
                                System.out.println("Test "+(1+testData.lastIndexOf(testCase))+" Passed " +obtainedResult+"= obtainedResult "+expectedResult+"= expectedResult");
                        else
                                System.out.println("Test "+ (1+testData.lastIndexOf(testCase))+" Failed "+obtainedResult+"= obtainedResult "+expectedResult+"= expectedResult");
                        
                }
      
        }
		
		
		

	}


