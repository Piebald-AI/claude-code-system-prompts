<!--
name: "Data: Ship existing pull request commit and push terms"
description: "Explains when /ship commits and pushes work to an existing private pull request and how background agents and an earlier watch affect that preparation"
ccVersion: "2.1.331"
-->
- Where your own pull request is open and checked out here, Claude Code also commits your uncommitted changes, in the same way, and pushes them and your unpushed commits onto it. It does so only in a terminal, and only if your branch holds every commit of the one on GitHub, no merge or rebase is under way, no hosted agent is working on it, auto-merge is off, and the repository isn't public. Otherwise your unpushed commits go up with my first push, if I make one. While an agent of mine is still at work in the background in this session, Claude Code commits nothing, and if you have uncommitted changes it pushes nothing either. If I'm already watching it in this session, that watch ends first.
