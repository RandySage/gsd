..    Copyright 2014, R.Sage (http://github.com/ransage)
      This source (rst) is subject to the
      terms of the Mozilla Public License, v.
      2.0. If a copy of the MPL was not
      distributed with this file, You can
      obtain one at
      http://mozilla.org/MPL/2.0/.


.. GSD documentation master file, created by
   sphinx-quickstart on Sun Jan 12 16:24:31 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GSD's documentation!
===============================

A system and eventually some software used to Get S@#$% Done

.. Warning:: This documentation is pre-release and is probably not suitable for use.  Users beware! (better yet, check back later)

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Foreword
--------

License
~~~~~~~

Although this repo will start as documentation, it will initially be in sphinx and therefore making 'source' available does seem logical.  I like collaborative and free (libre) endeavors, but it is valuable to me to maintain control over my own version of documentation.  For that reason, when the system starts to come together I might choose to submodule the docs (or at least portions thereof) and revise the licenses on each of the two projects to better reflect intended usability.

Also, until contributions are taken from others, it is easy to license content under other terms.  Feel free to contact us and we may be amenable to licensing under the terms of your choice.  (This is probably most easily accomplished - and documented - by having us fork, contribute, and issue pull request for your project, assuming you have clear license terms.

Terms
~~~~~

GTD vs. 'GTD': The letters GTD are widely used for the philosophy and/or the mechanics/system described by David Allen in his book "Getting Things Done".  This includes broad usage for adaptations of the system, which seems fair since 'GTD' seems to lay out a philosophy and encourage tailoring in addition to providing you a system for GTD.  I will attempt to use 'GTD' or "GTD" (in some kind of quotes) to refer to the actual book he published whereas I'll bow to common usage of GTD (without quotes) to refer to broader philosophy or the act of following one of the many systems.

System
------

The intent is to document the system(s) used with GTD-style task management, as well as the underlying hypotheses that David Allen's system seem to be addressing.  You should probably read "Getting Things Done" before you attempt to begin adapting a system that has worked for so many people.  If you find his proposed systems do not meet your needs, then you might benefit from this - or it might confuse and derail you.  I make no warranties.

Getting things just right
~~~~~~~~~~~~~~~~~~~~~~~~~

This style of systems has a great deal of process, which is essential to applying the techniques.  For a given process, the actual tools (e.g., software or even paper systems) need not significantly alter the workflow, but in my case I always find that they do.

Additionally, I find that there is a spectrum of users with both extremes and the middle all found in my household:
  - I like things complicated, I have scores of incubating projects that may or may not ever get worked and I want to track them all while knowing that I won't lose anything, but without getting overwhelmed
  - My roommate has a super simple, but limited system - she does not tolerate incomplete projects, she keeps a few things in her head, she has appointments in her calendar, and she uses shopping lists.
  - My partner is Goldilocks - she has reasonable needs and finds my system way too big, but the simple paper system too cramped.  My partner needs more structure than our roommate's system can provide, but finds my system overwhelming and unhelpful.
  
Whatever your needs, the emphasis should be on getting your system just right so that it gives you all the features you need with a minimum amount of inefficiency or overhead.  Throughout I focus on medium and high complexity systems because I believe that the 'GTD' system is superb for anybody with basic needs. 
  
Initial system
--------------

The complicated system
~~~~~~~~~~~~~~~~~~~~~~

Initially, I am using django-gtd to manage my complicated system.  I find that it is quite well implemented in general and that it works passably for my needs, although I found that documentation would have been very helpful (I'll remedy that) and there are a few features that either are broken or that I have misconfigured (ticklers and emails) and recurring tasks does not seem to be a feature.

Medium system
~~~~~~~~~~~~~

I have one client who uses a restricted system, so I use a very simple, client-specific system there that uses a variant of the 'GTD' paper method, in which I use imap folders as if they were paper folders and I file one item (an email) per task or project into the appropriate next actions, waiting, projects, etc. folders.  I think that this type of system may be sufficient for most people and for my partner.  
Thus, I think I may develop a simple, lightweight app that sits on top of the imap folder, sets up the structure, and provides the workflow cues to make this even easier for my partner - it will help me too with my client.  Having played with python and email before, the first prototype will likely be a 

Long term system
----------------

My long term system will be a unified portal for all of my digital life.  This portal will consist either entirely of open source software or of interface-standardized elements that I am able to substitute (i.e. I don't mind having a closed source element if it is better than the open source alternative, so long as it conforms to the interface standard allowing me to switch back to open source when time permits me or others to enhance the open source option).  (( FN: In this instance, emphasis on 'open source' is because this system is so important to me that I do not want to entrust key parts of it to black box, commercial systems.  I want to see the gears turning inside. ))  My data will be stored either exclusively in my systems (with my remote backups) or will be stored with trusted vendors.  Ideally, this system will just make it easier to do tasks I already do, but will allow me to integrate my informal map of my systems into an enhanced workflow.

Finally, this system *requires* digital filing/reference system.  This feature is something I really struggle with at present, but that is a project unto itself.  For now, I'm using a combination of paper and digital file systems for reference because digitizing papers is not efficient enough and because I struggle to file things suitably when they are digital. 

.. Todo:: Figure out how to implement footnotes.

.. Todo:: insert mind map showing mess of 'systems' I currently have.



Use others' documentation
===========
Read "Getting Things Done" by David Allen - the material here is really a supplement to that material.

I also recommend "The Now Habit" as it covers a number of similar thought patterns that can interfere with getting your s*)(& done.

For additional motivation, I'm fond of "The Cult of Done Manifesto": http://www.flickr.com/photos/joshuarothhaas/3327763912/


Weekly review
============

The documentation at lifehacker provides an excellent summary on this topic: http://lifehacker.com/5908816/the-weekly-review-how-one-hour-can-save-you-a-weeks-worth-of-hassle-and-headache




Dedicated (sub)system
===============

For my client who has a restricted computing system, I have a dedicated sub-system.  I use an IMAP folder based approach.  This is great because they have a secure, remote email access system that then lets me access my stuff from anywhere.  I use the following folder structure:

.. todo:: fix that sphinx does not produce monospaced output for the following directory tree
..
|        ├── @actions
|        │   └── deferred
|        ├── @projects
|        │   └── tickler
|        └── @waiting

Note that this does not distinguish any of the various contexts that I might have for other clients or for myself.  This is because I choose to keep this system very simple.  As a result, I need to be especially careful to limit the number of next actions to an absolute minimum, which is not too hard because things are typically so frantic there that only one or two things are worked until their conclusion and then other things are selected.


Notes on headers - top / first level with '=' H1
================

Second level with '-' H2
-------------

Third level with '~' H3
~~~~~~~~~~~~~~

Fourth level with '%' (TBR) H4
%%%%%%%%%%%%%%%%%%%%
