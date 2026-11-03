<!--
name: "Data: SDK result credential_expires_at field"
description: "Documents the stored claude.ai login expiration timestamp on numbered results, including refresh-chain lifetime, estimate uncertainty and omission rules"
ccVersion: "2.1.318"
-->
When the claude.ai credential this process's requests send ends for good, as an ISO 8601 instant, read as the result is written. For a stored claude.ai login it is the end of the login's refresh chain as stored at sign-in, which renewing the access token does not move. That date is the server's when it sent one and otherwise a 30-day estimate, and the real end can be up to 3 days earlier. The server is not asked, so a login revoked early still shows its date, and a date in the past means the login has probably ended, not that it has. Absent when no date is known, for every other credential (an API key, a token from the environment, another provider), on results this process did not number, and from older producers.
