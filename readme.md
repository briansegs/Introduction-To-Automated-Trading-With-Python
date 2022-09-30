# Introduction-To-Automated-Trading-With-Python

## Goals
This project's purpose is to help me get started with Kucoin's API and the tools needed for trading.
Tasks:
- Pull coin data from the API and display it in a readable format
- Create logic for entering and exiting trades
- Create an experience that feels good (play)

## Notes
This app does not execute live trades but it is set up to do so.
There are a few reasons I decided against live trading:
- The app calls the API too many times and will produce an error before the trade completes
- Using Websockets would be the correct way to approach this.
- Websockets are out of the scope of this project.
If you would like to execute live trades:
- import trading tools
- Add order flow to trade logic
I will add orders to future projects. Even though there is a chance of the app not crashing before a trade is completed,
It's not worth it. I feel good about what was completed and I consider this project a success for what it is.