# About this challenge

This is the 5th challenge of the Shopee Code League 2020. The competition details can be found [here](https://www.kaggle.com/c/logistics-shopee-code-league/overview).


My notebook can be found in this folder, named 'Shopee #5.ipynb'. The accuracy I obtained for my submission was 0.37134.

# Some thoughts

I am acutely aware that my solution is by no means perfect, and the accuracy is certainly not anything to be wowed by. This section serves as a reflection for me to evaluate the shortfalls of my solution, and what I could and should have done better with more time.
    
1. **My solution did not take into account the SLA matrix.**
    * *Why did I not do this?*
      * Time constraint
      * Did not quite know how to go about doing it. I had the idea of taking the last few words of the buyer and seller addresses, as it contained the countries in the SLA matrix, but did not have the time within the 3 hours to fully look into it and execute. 
    
    
    * Looking at solutions after the challenge ended, I realised that I should have put the information from the matrix in a dictionary and create a list of holidays in March (as the orders in the csv are for March).
    
2. **Converting the epoch time using *time* and *datetime* rather than using pandas's *to_datetime* instead.**
    * While this is not a major downfall, using *to_datetime* will reduce the number of steps in the solution.
      
      
