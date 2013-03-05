Formulagame
===========

A simple turn-based formula game, created with Python and PyQt4 for a programming course in Aalto University.

The rules are as follows:
MOVING: 
  Cars have 5 gears. The speed and the turn radius depends on the gear.
    - On every turn, the player can change the gear one step up or down.
    - Also, the car can be turned by one step per turn.
    - When changing the gear, the direction of the car is the one that's closer
    to the last turn's direction. This is calculated by using arcsin of both moves
    and comparing them to each other.

   The move options for all five geas have been presented below:

      (1)    (2)      (3)       (4)         (5)

                                       ***********
                            *********  *         *
                   *******  *       *  *         *
           *****   *     *  *       *  *         *
     ***   *   *   *     *  *       *  *         *
     *A*   * A *   *  A  *  *   A   *  *    A    *
     ***   *   *   *     *  *       *  *         *
           *****   *     *  *       *  *         *
                   *******  *       *  *         *
                            *********  *         *
                                       ***********

  For example, a car driving on gear 2, the car would turn 90 degrees like this:

           0.1.         
               .2   
                 .    
                  3
                  ..
                   4
                   .
                   5

  Example 2, a car moving on gear 1 and turning 90 degrees:

          01         
            2   
            3   

  Example 3, a car changing gear up between the moves and turning at the same time:

          01.
            .2
              ..
                3
                 ..           
                  ..
                    4
                     .
                      .
                       .
                        5

GENERAL:
  The players move their cars one by one, based on the moving rules described above.
    - Both cars start the race by facing right.
    - If a player drives out of the road, the game ends and he loses. The player has to stay
    on the road, on every point between the initial point and the end point. This is checked by using
    Bresenham's algorithm.
    - Two cars cannot be on the same point at the same time. If the player hits the opponent, he loses.
    - The winner is the player, who drives over the finish line first.
