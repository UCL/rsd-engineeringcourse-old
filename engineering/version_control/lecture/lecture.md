% Practical Version Control and Issue Tracking
% James Hetherington

Practical Version Control and Issue Tracking
--------------------------------------------

Managing Code Inventory

  - "When did I introduce this bug"?
  - Undoing Mistakes

Working with other programmers

  - "How can I merge my work with Jim's"

What's the most important bug to fix next?

What is version control?
------------------------

Do some programming

    my_vcs commit

Program some more

Realise mistake

    my_vcs rollback

Mistake is undone

What is version control? (Team version)
---------------------------------------

Sue                 James
------------------ ------
Create some code    
`my_vcs commit`     
                    Join the team
                    `my_vcs checkout`
                    
Distributed team workflow with conflicts
----------------------------------------
![Image showing workflow](assets/distributed_shared_conflicted.pdf)\