Formulagame
===========

Simple turn-based formula game, created with Python and PyQt4.

The game is developed for a course programming course in Aalto University.

The rules are as follows:

Moving: 
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
