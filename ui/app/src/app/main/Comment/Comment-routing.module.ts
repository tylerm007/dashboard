import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CommentHomeComponent } from './home/Comment-home.component';
import { CommentNewComponent } from './new/Comment-new.component';
import { CommentDetailComponent } from './detail/Comment-detail.component';

const routes: Routes = [
  {path: '', component: CommentHomeComponent},
  { path: 'new', component: CommentNewComponent },
  { path: ':CommentId', component: CommentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Comment-detail-permissions'
      }
    }
  }
];

export const COMMENT_MODULE_DECLARATIONS = [
    CommentHomeComponent,
    CommentNewComponent,
    CommentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CommentRoutingModule { }