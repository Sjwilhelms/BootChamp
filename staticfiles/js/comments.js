const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/** Initialises edit functionality for the provided edit buttons 
 * 
 * for each button in the 'editButtons' collection:
 * -retireved the associated comments id on click
 * -fetches the content of the corresponding comment
 * -populated the 'commentText' input/textarea with the comment's content for editing
 * - updated the submit buttons text to "Update"
 * -sets the forms action attribute to the 'edit_comment/{comment_id}' endpoint
*/

for(let button of editButtons){
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}

/** Initialises deletion functionality for the provided delete buttons.
 * 
 * For each button in the 'deleteButtons' collection:
 * - retireves the associated comment's ID upon click
 * - updates the 'deleteConfirm' link's href to point to the deletion endpoint for the specific comment
 * -displays a confirmation modal ('deleteModal') to prompt the user for confirmation before deletion
 */

for(let button of deleteButtons){
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}