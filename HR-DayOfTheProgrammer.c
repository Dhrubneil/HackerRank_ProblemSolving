#include<stdio.h>
#include<string.h>
#include<stdlib.h>

//Programmer day is the 256th day of a calendar year- both in Gregorian and Julian
//In Russia the transition from Julian to Gregorian occurred in 1919
char* programmerDay(int year){
    char* date = malloc(100*sizeof(char));
    if(year >= 1919){
        if(year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)){
            sprintf(date, "12.09.%d", year);
        }
        else{
            sprintf(date, "13.09.%d", year);
        }

    }
    else if(year == 1918){
        return "26.09.1918"; //In 1918, Julian calender lost it's 14 days after January 31st while it was Russia's official calender
            //That is, February 14th was the 32nd day of the year 1918 in Russia
    }
    else{
        if(year % 4 == 0){  //In Julian calendar, if this only condition is met by a year, that is a leap year
            sprintf(date, "12.09.%d", year);
        }
        else{
            sprintf(date, "13.09.%d", year);
        }
    }


    return date;
}

char* myName(int x){
    char* name = malloc(100*sizeof(char));
    name = "Niloy";
    return name;
}
int main(){
    char date[10];
    printf("\nEnter Date: ");
    scanf("%s", date);
    printf("\nDate = %s\n", date);
    printf("Enter Year: ");
    int year;
    scanf("%d", &year);
    printf("\nYear = %d\n", year);

    char year_c[4];
    sprintf(year_c, "%d", year); // converting a number to a string
    printf("\nYear = %s\n", year_c);

    char mydate[10] = "12.09.";
    strcat(mydate, year_c);
    printf("\nMy Date = %s\n", mydate);


    //printf("\nProgrammer's Day: %s", programmerDay(2000));
    char* result = programmerDay(1800);
    printf("\nP D: %s\n", result);

    char* name = myName(10);
    printf("\nName = %s\n", name);

}
