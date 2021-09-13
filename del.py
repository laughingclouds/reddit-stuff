"""I have some doubts regarding this, I shouldn't depend on importing the module
to run the code. Maybe I should use a function and only that function should be available
to any files importing the module.

The ability to take a subreddit instance as an arguement and using that instance to post
would also be nice. Maybe I shouldn't even initialize the reddit and subreddit instance
in modules that are meant to be imported.

NOTE: It would be nice if `GallerySubmit` also returns the link(s) to the post it submitted to.
In fact if every other submission related module does this it would be nice."""
import GallerySubmit
