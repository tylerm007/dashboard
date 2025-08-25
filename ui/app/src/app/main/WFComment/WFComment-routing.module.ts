import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WFCommentHomeComponent } from './home/WFComment-home.component';
import { WFCommentNewComponent } from './new/WFComment-new.component';
import { WFCommentDetailComponent } from './detail/WFComment-detail.component';

const routes: Routes = [
  {path: '', component: WFCommentHomeComponent},
  { path: 'new', component: WFCommentNewComponent },
  { path: ':CommentID', component: WFCommentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WFComment-detail-permissions'
      }
    }
  }
];

export const WFCOMMENT_MODULE_DECLARATIONS = [
    WFCommentHomeComponent,
    WFCommentNewComponent,
    WFCommentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WFCommentRoutingModule { }