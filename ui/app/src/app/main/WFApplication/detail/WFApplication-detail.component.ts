import { Injector, ViewChild, Component, OnInit, ViewEncapsulation } from '@angular/core';
import { OFormComponent, OntimizeService, OListPickerComponent, OTableComponent, ORealPipe, ONIFInputComponent } from 'ontimize-web-ngx';


@Component({
  selector: 'WFApplication-detail',
  templateUrl: './WFApplication-detail.component.html',
  styleUrls: ['./WFApplication-detail.component.scss']
})
export class WFApplicationDetailComponent implements OnInit  {
  protected service: OntimizeService;
  public data: any;

  @ViewChild('oDetailForm') form: OFormComponent;
  
  constructor(protected injector: Injector) {
    this.service = this.injector.get(OntimizeService);
  }

  ngOnInit() {
    this.configureService();
  }

  protected configureService() {
    const conf = this.service.getDefaultServiceConfiguration();
    conf['path'] = '/WFApplication';
    this.service.configureService(conf);
  }
  onDataLoaded(e: object) {
    this.data = e;
    console.log(JSON.stringify(e));
  }
  start_workflow() {
    // Implement workflow start logic here
    console.log("Starting workflow...");
    //ServiceRequestParam<T> = {
    //method: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
    //url: string;
    //body?: any;
    this.service.doRequest({method: 'GET', url: 'http://localhost:5656/start_workflow?application_id=' + this.data.ApplicationID}).subscribe((resp) => {
      console.log("res: " + JSON.stringify(resp));
      if (resp.code === 0) {
        console.log('workflow started successfully')
      }
    });
  }
}