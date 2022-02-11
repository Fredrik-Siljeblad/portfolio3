//https://yh.pingpong.se/courseId/13958/content.do?id=6429864


//Object account
const account = {
    accountName: "Fredrik Jonsson",
    balance: 100,
    getBalance: function(){return this.balance;},
    deposit: function(amount){this.balance += amount;},
    withdrawal: function(amount){this.balance -= amount;},
    getAccountName: function(){return this.accountName;},
    accountError: function(str = "Unexpected Error!"){
        //Simply using this method to alert the user when something unexpected happened.
        //Normally an error message is provided, but just in case...
        alert(str);
    },
    exitAccount: function(){
        let message = document.getElementById("message");
        console.log(message);
        message.innerHTML = "Welcome Back!";
        return;
    }
}

atm();

//Function atm
function atm(){
    menu1();
    
    function menu1(){
        let choice = prompt(
            `Select a choice:
            1.) See the balance
            2.) Make a deposit
            3.) Make a withdrawal
            4.) Get account name
            5.) Exit `,
            "Enter Choice");
        //Here Switch is chosen over If/Else as I find it cleaner and easier to read
        //when there are distinct choices.
        switch(choice){
            case "1":
                alert(`Your current balance: ${account.getBalance()}`);
                menu1();  
                break;
            case "2":
                menu2();
                break;
            case "3":
                menu3();  
                break;
            case "4":
                alert(`Name of account: ${account.getAccountName()}`);
                menu1();  
                break;
            case "5":
                account.exitAccount();
                break;
            default:
                account.accountError("Sorry, you must make a choice from the menu."); 
               menu1();                                         
        }
        
    }

    function menu2(){
        //Using parseFloat to turn the string from prompt into a numeric value (or a non-numeric to be catched as invalid)
        let choice = parseFloat(prompt(
            `How much would you like to deposit?`, "Enter Amount"));
        //Here If/Else is used over Switch as I find it easier to handle more complex conditionals.
        if(isNaN(choice)){
            account.accountError("You must enter a numeric amount.");
            menu2();
        }else if(choice <= 0){
            account.accountError("You cannot deposit 0 or less.");
            menu2();
        }else{
            account.deposit(choice);
            menu1();
        }
       
    }

    function menu3(){
        //Using parseFloat to turn the string from prompt into a numeric value (or a non-numeric to be catched as invalid)
        let choice = parseFloat(prompt(
            `How much would you like to withdraw?`, "Enter Amount"));
        //Here If/Else is used over Switch as I find it easier to handle more complex conditionals.
        if(isNaN(choice)){
            account.accountError("You must enter a numeric amount.");
            menu3();
        }else if(choice <= 0){
            account.accountError("You cannot withdraw 0 or less.");
            menu3();
        }else if(choice > account.getBalance()){
            account.accountError(`You cannot withdraw ${choice} as your balance is only ${account.getBalance()}`);
            menu3();
        }else{
            account.withdrawal(choice);
            menu1();
        }
    }
}