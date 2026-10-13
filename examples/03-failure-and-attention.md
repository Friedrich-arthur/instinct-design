# Be honest about failure and selective about interruption

Synthetic design example. A video file has been exported. Upload to the publishing platform failed. The draft and export remain saved. No publication deadline is specified.

## Before

> Task completed successfully! Your content generation workflow is finished. A publishing connector error occurred. Please see logs.

## After

> The video is exported, but the post is not published. Your draft is saved. Retry the upload when you're ready.

The primary action is "Retry upload". The expanded view provides the platform error, the saved file, and the last upload attempt. Retrying the same task does not create a second post if the first attempt later succeeds; that behavior must be implemented and tested.

## If a deadline becomes relevant

If the user requested publication by 17:00 and a recoverable upload failure threatens that deadline, notify them with the failure and the remaining action. Without a meaningful deadline or requested alert, record the result in the task view or digest.

## What changed

Partial success remains partial success. The result survives the error in the design contract. The notification decision follows the user's consequence rather than an internal event.
