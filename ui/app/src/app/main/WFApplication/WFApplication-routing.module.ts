import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WFApplicationHomeComponent } from './home/WFApplication-home.component';
import { WFApplicationNewComponent } from './new/WFApplication-new.component';
import { WFApplicationDetailComponent } from './detail/WFApplication-detail.component';

const routes: Routes = [
  {path: '', component: WFApplicationHomeComponent},
  { path: 'new', component: WFApplicationNewComponent },
  { path: ':ApplicationID', component: WFApplicationDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WFApplication-detail-permissions'
      }
    }
  },{
    path: ':ApplicationID/Company', loadChildren: () => import('../Company/Company.module').then(m => m.CompanyModule),
    data: {
        oPermission: {
            permissionId: 'Company-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/Contact', loadChildren: () => import('../Contact/Contact.module').then(m => m.ContactModule),
    data: {
        oPermission: {
            permissionId: 'Contact-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/Ingredient', loadChildren: () => import('../Ingredient/Ingredient.module').then(m => m.IngredientModule),
    data: {
        oPermission: {
            permissionId: 'Ingredient-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/Plant', loadChildren: () => import('../Plant/Plant.module').then(m => m.PlantModule),
    data: {
        oPermission: {
            permissionId: 'Plant-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/Product', loadChildren: () => import('../Product/Product.module').then(m => m.ProductModule),
    data: {
        oPermission: {
            permissionId: 'Product-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/ValidationCheck', loadChildren: () => import('../ValidationCheck/ValidationCheck.module').then(m => m.ValidationCheckModule),
    data: {
        oPermission: {
            permissionId: 'ValidationCheck-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/WFActivityLog', loadChildren: () => import('../WFActivityLog/WFActivityLog.module').then(m => m.WFActivityLogModule),
    data: {
        oPermission: {
            permissionId: 'WFActivityLog-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/WFComment', loadChildren: () => import('../WFComment/WFComment.module').then(m => m.WFCommentModule),
    data: {
        oPermission: {
            permissionId: 'WFComment-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/WFFile', loadChildren: () => import('../WFFile/WFFile.module').then(m => m.WFFileModule),
    data: {
        oPermission: {
            permissionId: 'WFFile-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/WFMessage', loadChildren: () => import('../WFMessage/WFMessage.module').then(m => m.WFMessageModule),
    data: {
        oPermission: {
            permissionId: 'WFMessage-detail-permissions'
        }
    }
},{
    path: ':ApplicationID/WFQuote', loadChildren: () => import('../WFQuote/WFQuote.module').then(m => m.WFQuoteModule),
    data: {
        oPermission: {
            permissionId: 'WFQuote-detail-permissions'
        }
    }
}
];

export const WFAPPLICATION_MODULE_DECLARATIONS = [
    WFApplicationHomeComponent,
    WFApplicationNewComponent,
    WFApplicationDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WFApplicationRoutingModule { }