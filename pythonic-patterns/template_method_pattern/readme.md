# Template Method Pattern
- Allows sepertion between components and algorithm implementation. 
  - Notice how "trading_bot.py" contains the abstract class with the trade logic.
- **When to use the template method?**
  - Function with many varieties. Move the variety into separate methods and have subclasses that implement them (i.e bitcoin and ethereum that inherit from the abc tradingbot w/ common trading algorithm). To split things up more you can take a functional approach and even implement protocol segregation.

### Classic
- Strategy is nothing more than a glorified higher order function
- Covered using classes (inheritance with abc or ducktyping with protocols) or a functional approach for abstraction
- Use where you have long if else statements to simplify your code

### Functional
- Can also decide to take a functional approach, but remember that the goal is to aim for readibility.


### Functional V2
- Example of protocol segregatoion. Separation of the engine from the trading strategy.
